function makeTimer() {
  const m = new Motherboard();
  m.addDevice(new MMU(new RAM(256)));
  const c = new CPU(m);
  m.addDevice(c);
  const t = new Timer();
  m.addDevice(t);
  return [m, c, t];
}


function sleep(ms) {
  const d = (Date.now() + ms) >>> 0;
  while(d > (Date.now() >>> 0)) { }   // busy wait
}


test('Timer: sanity', t => {
  t.doesNotThrow(() => new Timer(), null, "timer created");
  t.doesNotThrow(() => makeTimer(), null, "timer created and added to motherboard");
  t.end();
});


test('Timer: clock', t => {
  const [mb, cpu, tm] = makeTimer(); 
  const d = new Date(2016, 1, 1).valueOf();

  mb.step();
  
  const cp_now = (Date.now() - d) >>> 0;
  const vm_now = mb.get32(tm.TM_CLOCK);

  t.pass((vm_now >= cp_now - 10000) && (vm_now <= cp_now + 10000), 
      `times match 0x${vm_now.toString(16)} (VM) vs 0x${cp_now.toString(16)}`);

  t.end();
});


test('Timer: counter', t => {
  const [mb, cpu, tm] = makeTimer(); 
  
  mb.set32(tm.TM_TIMER0, 1000);
  sleep(100);
  mb.step();
  const v = mb.get32(tm.TM_COUNTER0);
  t.notEqual(v, 0, 'counter != 0');
  t.pass(v > 50, 'counter > 50');

  t.end();
});


test('Timer: interrupt', t => {
  const [mb, cpu, tm] = makeTimer(); 

  mb.set(0x0, 0x86);  // nop
  mb.set32(cpu.CPU_INTERRUPT_VECT + (4 * mb.get(tm.TM_INTERRUPT)), 0x1000);
  cpu.T = true;

  mb.set32(tm.TM_TIMER1, 50);  // setup timer
  sleep(100);
  mb.step();

  t.equal(cpu.PC, 0x1000, 'interrupt was called');
  t.equal(mb.get(tm.TM_CUR_INT), 0x1, 'the correct interrupt was called');

  t.end();
});


// vim: ts=2:sw=2:sts=2:expandtab
