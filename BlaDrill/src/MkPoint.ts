import { MkShape } from './MkShape';

export class MkPoint implements MkShape {
  
  X : number;
  Y : number;
  Z : number;
  
  constructor ( x : number, y : number, z : number) {
    this.X = x;
    this.Y = y;
    this.Z = z;
  } 

  Length () : number {
    return 0;
  }

  DistanceFrom (pnt : MkPoint) : number {

    let dist = Math.sqrt(pnt.X - this.X)
    return 0;
  }

  Set(x : number, y : number, z : number) : void {
    this.X = x;
    this.Y = y;
    this.Z = z;
  } 


}