import test from 'tape';

import Motherboard from '../src/motherboard';
import RAM from '../src/ram';
import MMU from '../src/mmu';
import CPU from '../src/cpu';

import BIOS from '../src/bios';


test('BIOS: code', t => {
  function loader() {
    return new Uint8Array([0, 1, 2, 3, 4]);
  }

  const mb = new Motherboard();
  mb.addDevice(new MMU(new RAM(256)));
  const cpu = new CPU(mb);
  mb.addDevice(cpu);
  const bios = new BIOS(loader);
  mb.addDevice(bios);

  t.equals(mb.get(bios.BIOS_CODE + 2), 2, 'BIOS code loaded');
  t.equals(cpu.PC, bios.BIOS_CODE, 'CPU pointing to BIOS code');

  t.end();
});


// vim: ts=2:sw=2:sts=2:expandtab
