"use strict";
exports.__esModule = true;
exports.MkPoint = void 0;
var MkPoint = /** @class */ (function () {
    function MkPoint(x, y, z) {
        this.X = x;
        this.Y = y;
        this.Z = z;
    }
    MkPoint.prototype.Length = function () {
        return 0;
    };
    MkPoint.prototype.DistanceFrom = function (pnt) {
        var dist = Math.sqrt(pnt.X - this.X);
        return 0;
    };
    MkPoint.prototype.Set = function (x, y, z) {
        this.X = x;
        this.Y = y;
        this.Z = z;
    };
    return MkPoint;
}());
exports.MkPoint = MkPoint;
