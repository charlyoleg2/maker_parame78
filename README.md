maker\_parame78
===============


Presentation
------------

This repo is a maker-repository. It stores the parameters and the STL-files of parts made with *desi78*.
This repo uses the javascript packages [desi78-cli](https://www.npmjs.com/package/desi78-cli) and [desi78-uis](https://www.npmjs.com/package/desi78-uis) of the design-library [desi78](https://charlyoleg2.github.io/parame78/).


Requirements
------------

- [node](https://nodejs.org) > 22.00.0
- [npm](https://docs.npmjs.com/cli) > 11.0.0


### Optional requirements

- [OpenSCAD](https://openscad.org/)

For Ubuntu users, *OpenSCAD* is available on [snapcraft](https://snapcraft.io/openscad) and can be installed with:

```bash
sudo snap install openscad
```

Upgrade
-------

For working with the latest *desi78* version:

```bash
npm outdated
npm update --save
git commit -am 'npm update --save'
```


Dev
---

```bash
git clone https://github.com/charlyoleg2/maker_parame78
cd maker_parame78
npm install
npm run
npm run desi78-uis
npx desi78-uis
npx desi78-cli --help
./make_parts.js
```

Vocabulary
----------

- Design: A parametrizable 3D parts. Desginix is a collection of designs.
- Part or Reference: A particular parametrization of a design.
- Instance: The realization of a reference.


References for the maker\_parame78
----------------------------------

ID | Reference           | Design             | Nb of instances
---|---------------------|--------------------|----------------
1  | door                |  door              | 1
2  | maison              |  maison            | 1
3  | cabane\_plancher    |  cabane\_plancher  | 1
4  | cabane              |  cabane            | 1
5  | reinforced\_tube    |  reinforced\_tube  | 1
6  | reinforced\_cone    |  reinforced\_cone  | 1
7  | lens\_x1            |  lens\_x1          | 1
8  | lens\_x3            |  lens\_x3          | 1
9  | pulley              |  pulley            | 1
10 | codeExample1        |  codeExample1      | 1
11 | rail                |  rail              | 1

Each reference has its own directory with its json-parametrization, scad-script and stl-file.


