import TinyVM from './tinyvm';
import Debugger from './debugger';

if (typeof window !== 'undefined') {
  window.TinyVM = TinyVM;
  window.Debugger = Debugger;
}

// vim: ts=2:sw=2:sts=2:expandtab
