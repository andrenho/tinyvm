'use strict';

class BIOS extends Device {

  constructor(biosCode) {
    super();
    this._const = this.constantList();
    if (!biosCode instanceof Uint8Array) {
      throw new Error('Invalid BIOS code.');
    }
    this._code = biosCode;
  }

  name() { return 'LuisaBIOS'; }
  deviceType() { return Device.Type.BIOS; }
  version() { return 0x0; }
  hasInterrupt() { return false; }
  memorySize() { return 0x10000; /* (64 kB) */ }

  constantList() {
    return {
      BIOS_TYPE:       0x00,
      BIOS_VERSION:    0x01,
      BIOS_INTERRUPT:  0x02,
      BIOS_NAME:       0x03,
      BIOS_CODE:       0x10,
    };
  }


  get(a) {
    if (a < 0x10) {
      return super.get(a);
    } else if (a >= 0x10 && a < (this._code.length + 0x10)) {
      return this._code[a - 0x10];
    }
    return 0;
  }


  set(a, v) {
    if (a < 0x10) {
      super.set(a, v);
    }
  }

}

// vim: ts=2:sw=2:sts=2:expandtab
