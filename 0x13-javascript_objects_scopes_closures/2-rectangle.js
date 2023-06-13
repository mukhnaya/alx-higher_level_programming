#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h > 0) {
      this.wdith = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
