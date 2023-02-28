'use strict';
// Canvas
const canvas = document.querySelector('canvas.webgl')
// System.import('./built/mklib.js');

// Sizes
const sizes = {
    width: 800,
    height: 600
}

"use strict";
var exports = {}
exports.__esModule = true;
var mklib = require("./built/mklib.js");
var pnt = new mklib.MkPoint(0, 0, 0);

// import * as mklib from './built/mklib.js';
// let shape = new mklib.MkPoint(0,0,0);
// console.log(shape);
// shape = 2;
// shape=2;//.Set(0,0,0)


// Scene
const scene = new THREE.Scene()

// Object
const cubeGeometry = new THREE.BoxGeometry(1, 1, 1)
const cubeMaterial = new THREE.MeshBasicMaterial({
    color: '#00ff88'
})
const cubeMesh = new THREE.Mesh(cubeGeometry, cubeMaterial)
scene.add(cubeMesh)

// Camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height)
camera.position.z = 3
scene.add(camera)

// Renderer
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.render(scene, camera)


