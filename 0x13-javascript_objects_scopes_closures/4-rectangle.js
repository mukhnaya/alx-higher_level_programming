#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const convenienceVar = this.width;
    this.width = this.height;
    this.height = convenienceVar;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
