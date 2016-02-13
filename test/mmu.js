import test from 'tape';

import RAM from '../src/ram';
import MMU from '../src/mmu';

// 
// VMEM disabled
//

test('MMU: translation (VMEM disabled)', t => {
  let m = new MMU(new RAM(4));
  t.equal(m.translate(8), 8, 'translation');
  t.end();
});


test('MMU: physical memory access (VMEM disabled)', t => {
  let m = new MMU(new RAM(4));
  m.initializeConstants(0);
  t.equal(m.getMemory(3), 0, 'get byte');
  m.setMemory(3, 0xFF);
  t.equal(m.getMemory(3), 0xFF, 'get changed byte');
  t.equal(m.get(m.MMU_ERR), m.MMU_ERR_NONE, 'no errors');
  t.end();
});


test('MMU: physical memory size', t => {
  let m = new MMU(new RAM(4));
  m.initializeConstants(0);
  t.equal(m.get32(m.MMU_RAM_SZ), 4 * 1024, 'memory size register');
  t.end();
});


test('MMU: physical access out of bounds', t => {
  let m = new MMU(new RAM(4));
  m.initializeConstants(0);
  m.getMemory(0xEE0000);
  t.equal(m.get(m.MMU_ERR), m.MMU_ERR_OUT_OF_BOUNDS, 'access is out of bounds');
  t.end();
});


test('MMU: clear error', t => { 
  let m = new MMU(new RAM(4));
  m.initializeConstants(0);
  m.getMemory(0xEE0000);
  t.equal(m.get(m.MMU_ERR), m.MMU_ERR_OUT_OF_BOUNDS, 'error as expected');
  m.set32(m.MMU_ERR, m.MMU_ERR_NONE);
  t.equal(m.get(m.MMU_ERR), m.MMU_ERR_NONE, 'error is cleared');
  t.end();
});


//
// VMEM enabled
//

function mmu_vmem() {
  let m = new MMU(new RAM(256));
  m.initializeConstants(0);
  m._ram.set(0x4ABC, 0x1F);
  m._ram.set(0x1F0AC, 0x2B);
  m.set32(m.MMU_VMEM, 0x4 | (1 << 31));
  return m;
}

test('MMU: enabled VMEM', t => {
  let m = mmu_vmem();
  t.equal(m.get32(m.MMU_VMEM), (0x4 | (1 << 31)) >>> 0, 'VMEM register is correct');
  t.ok(m._vmem.active, 'VMEM is active');
  t.equal(m._vmem.page, 0x4, 'VMEM page is 0x4');
  t.end();
});

// vim: ts=2:sw=2:sts=2:expandtab