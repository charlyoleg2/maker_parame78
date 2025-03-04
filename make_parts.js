#!/usr/bin/env node
// make_parts.js

import { exec } from "child_process";
import { promisify } from 'util';

const c_Parts = {
	door: 'door_v01',
	maison: 'maison_v01',
	cabane_plancher: 'cabane_plancher_v01',
	cabane: 'cabane_v01',
	reinforced_tube: 'reinforced_tube_v01',
	reinforced_cone: 'reinforced_cone_v01',
	sfDie_A: 'sfDie_A_v01',
	sfDie_B: 'sfDie_B_v01',
	sfDie_C: 'sfDie_C_v01',
	sfDie_D: 'sfDie_D_v01',
	lens_x1: 'lens_x1_v01',
	lens_x3: 'lens_x3_v01',
	pulley: 'pulley_v01',
	codeExample1: 'codeExample1_v01',
	demoSheetFold: 'demoSheetFold_v01',
	demoSheetFold2_A: 'demoSheetFold2_A_v01',
	demoSheetFold2_B: 'demoSheetFold2_B_v01',
	demoSheetFold2_C: 'demoSheetFold2_C_v01',
	armEnd: 'armEnd_v01',
	armAxis: 'armAxis_v01',
	rail: 'rail_v01',
};

const c_svgdxf = {
	door: ['faceDoor', 'faceTop', 'faceSide'],
	maison: ['faceSide1', 'faceSide2', 'faceTop1', 'faceSide2', 'faceChimney'],
	cabane_plancher: ['facePlancherTop', 'facePlancherBottom', 'faceBeam', 'faceLeg', 'faceButtress', 'faceSide'],
	cabane: ['faceTop', 'faceFaceFront', 'faceFaceBack', 'faceFaceRoof', 'faceFaceSide', 'faceSide'],
	reinforced_tube: ['faceTopExt', 'faceTopWave', 'faceTopInt', 'faceSide'],
	reinforced_cone: ['faceTopWave', 'faceSideExt', 'faceSideInt', 'faceTopWaveH', 'faceTopWaveL'],
	sfDie_A: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	sfDie_B: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	sfDie_C: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	sfDie_D: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	lens_x1: ['faceLensSim', 'faceLens3D'],
	lens_x3: ['faceLensSim', 'faceLens1', 'faceLens2', 'faceLens3'],
	pulley: ['facePulleyProfile', 'facePulleyRim', 'facePulleyWidth'],
	codeExample1: ['faceExample1'],
	demoSheetFold: ['faceCut', 'facet1', 'facet3', 'SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	demoSheetFold2_A: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	demoSheetFold2_B: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	demoSheetFold2_C: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	armEnd: ['SFG_pattern', 'SFG_profiles', 'SFG_f00', 'SFG_f01', 'SFG_fj00'],
	armAxis: ['faceAxis', 'faceHoleS', 'faceHoleL'],
	rail: ['faceRail'],
};

function inferDesignName(instanceName) {
	const re = /_[A-Z][0-9]*$/;
	const rDesignName = instanceName.replace(re, '');
	return rDesignName
}

function getCmd(dName, fName) {
	const desiName = inferDesignName(dName);
	console.log(`info456: reference name: ${dName}   design name: ${desiName}`);
	const rCmd = [];
	//rCmd.push('pwd');
	//rCmd.push(`ls refs/${dName}`);
	//rCmd.push(`npx desi78-cli -d=desi78/${desiName} -o=refs/${dName} --outFileName=px_${fName}.json write json_param`);
	rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.log.txt write compute_log`);
	// svg, dxf
	for (const face of c_svgdxf[dName]) {
		rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.svg write svg__${face}`);
		rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.dxf write dxf__${face}`);
	}
	// paxJson
	rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.pax.json write pax_all`);
	// OpenSCAD
	rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.scad write scad_3d_openscad`);
	//rCmd.push(`openscad -o refs/${dName}/${fName}_oscad.stl refs/${dName}/${fName}.scad`);
	// JsCAD
	rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.js write js_3d_openjscad`);
	//rCmd.push(`cd refs && npx jscad ${dName}/${fName}.js -o ${dName}/${fName}_jscad.stl`);
	// FreeCAD
	rCmd.push(`npx desi78-cli -d=desi78/${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.py write py_3d_freecad`);
	//rCmd.push(`freecad.cmd refs/${dName}/${fName}.py refs/${dName}/${fName}_fc`);
	//rCmd.push(`npx rimraf refs/${dName}`);
	return rCmd
}

const aExec = promisify(exec);

async function execCmd(cmd) {
	console.log(cmd);
	try {
		const { stdout, stderr } = await aExec(cmd);
		console.log('---> stdout:');
		console.log(stdout);
		console.log('---> stderr:');
		console.log(stderr);
		console.log('---> end of log');
	} catch (err) {
		console.log(`err895: Error by executing: ${cmd}`);
		console.log(err);
		console.log(`info895: script stopped!`);
		process.exit(1);
	}
}

async function loopDesign(dList) {
	const pList = Object.keys(c_Parts);
	for (const [ idx, oneDesign ] of dList.entries()) {
		const idx2 = idx + 1;
		console.log(`${idx2} : working on ${oneDesign}`);
		if (!pList.includes(oneDesign)) {
			console.log(`err309: design ${oneDesign} is unkown!`);
			process.exit(1);
		}
		const cmds = getCmd(oneDesign, c_Parts[oneDesign]);
		for (const oneCmd of cmds) {
			await execCmd(oneCmd);
		}
		console.log(`${idx2} : end of generation of ${oneDesign}`);
	}
}

async function mhcli(args) {
	//console.log(args);
	const c_flag_all = '--all';
	const allList = Object.keys(c_Parts);
	if (args.length === 3 && args[2] === c_flag_all) {
		await loopDesign(allList);
	} else if (args.length > 2) {
		await loopDesign(args.slice(2));
	} else {
		console.log('err206: no argument provided!');
		console.log(`Possible arguments: ${c_flag_all} or the following design names:`);
		let str1 = '';
		let str2 = '';
		for (const [ idx, oneDesign ] of allList.entries()) {
			str1 += ` ${oneDesign}`;
			str2 += `${(idx + 1).toString().padStart(2, ' ')} : ${oneDesign}\n`;
		}
		console.log(str1);
		console.log(str2);
		console.log('info404: Nothing done!');
	}
}

console.log('make_parts.js says Hello!');
await mhcli(process.argv);
console.log('make_parts.js says Bye!');

