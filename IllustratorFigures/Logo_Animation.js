(function (cjs, an) {

var p; // shortcut to reference prototypes
var lib={};var ss={};var img={};
lib.ssMetadata = [];


// symbols:
// helper functions:

function mc_symbol_clone() {
	var clone = this._cloneProps(new this.constructor(this.mode, this.startPosition, this.loop));
	clone.gotoAndStop(this.currentFrame);
	clone.paused = this.paused;
	clone.framerate = this.framerate;
	return clone;
}

function getMCSymbolPrototype(symbol, nominalBounds, frameBounds) {
	var prototype = cjs.extend(symbol, cjs.MovieClip);
	prototype.clone = mc_symbol_clone;
	prototype.nominalBounds = nominalBounds;
	prototype.frameBounds = frameBounds;
	return prototype;
	}


(lib.Yellow = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FCD812").s().p("AJWUlQhahBj3i+Il7koImHkxQh+hlhAgwQh4hbgpilQAAgCgJgIIAAjRQAbhjBPhoICUivID5krIDFjkQBehyAwg4QBchtBygZQApgJA1AeQA0AdAbAsQAgAyASBLQALArARBYQA0D5BLF2IBxI6ICgMcQAIArAUBUQAOBLgCA3QgCBBgaAoQgcApgwAFIgRAAQhHAAhQg6g");
	this.shape.setTransform(87,137.5);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.Yellow, new cjs.Rectangle(0,0,174.1,275.1), null);


(lib.Red = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#CD2029").s().p("AGnLgQmSACimgFQingGlDABQlJAAifgFQhcgDgfgFQhFgMguglQg5gtAShCQAPg0AmgwQAcgjAzgsQBKg/CVh7QDei4BMg/QBfhRC9ijICUh6ICSh8QBShGANgKQA3gsAxgZQCXhNCuAsQCtAsBlCKQBQBtCBClIDVEPQDVESBRBuQBHBigNBfQgSCAimAgQgsAJhFABQhWAAg2ABQi8gLljABg");
	this.shape.setTransform(140.5,74.6);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.Red, new cjs.Rectangle(0,0,281,149.2), null);


(lib.Orange = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#F0692A").s().p("AszR7QgtgQgWgpQgLgVgPg9QgHgcgCgmIgChDQgDhigCjnQgCjTgFh1QgDg9ABivQAAiUgHhYQgHhRAAiIQABifgDg5QgHidBxiLQBxiLCXgXQADAAADgDIAFgGIImAAQAEALAMAAIASgBQBNACA1gCQBjgDC2AIQDCAIBYgBQBsgCBPA+QAvAlALA8QANBDgiBOQgTAqgmAxIhFBTIkMFHIjUD+IkCE7IjWEBIiECiQhPBhg3A/QgoAvhNBhQhHBVg6AxQgqAkgdAMQgWAKgXAAQgVAAgVgIg");
	this.shape.setTransform(95.4,115.5);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.Orange, new cjs.Rectangle(0,0,190.8,230.9), null);


(lib.Tween1 = function(mode,startPosition,loop) {
if (loop == null) { loop = false; }	this.initialize(mode,startPosition,loop,{});

	// Red Disk
	this.instance = new lib.Red();
	this.instance.parent = this;
	this.instance.setTransform(100.6,-249.5,1,1,0,0,0,140.5,74.5);
	this.instance.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.instance).to({alpha:1},47).to({_off:true},21).wait(277));

	// Orange Disk
	this.instance_1 = new lib.Orange();
	this.instance_1.parent = this;
	this.instance_1.setTransform(-86.6,-217.4,1,1,0,0,0,95.4,115.5);
	this.instance_1.alpha = 0;
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(30).to({_off:false},0).to({_off:true},38).wait(277));

	// Yellow Disk
	this.instance_2 = new lib.Yellow();
	this.instance_2.parent = this;
	this.instance_2.setTransform(-265,-84.5,1,1,0,0,0,87,137.6);
	this.instance_2.alpha = 0;
	this.instance_2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(47).to({_off:false},0).to({_off:true},21).wait(277));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-39.9,-324,281,149.2);


// stage content:
(lib.Logo_Animation = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Layer 1
	this.instance = new lib.Tween1("synched",0);
	this.instance.parent = this;
	this.instance.setTransform(678.8,398.9);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(68));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(1318.8,464.9,281,149.2);
// library properties:
lib.properties = {
	id: '50FC1612AB44944091A01156E58E0A1F',
	width: 1360,
	height: 780,
	fps: 100,
	color: "#FFFFFF",
	opacity: 1.00,
	manifest: [],
	preloads: []
};



// bootstrap callback support:

(lib.Stage = function(canvas) {
	createjs.Stage.call(this, canvas);
}).prototype = p = new createjs.Stage();

p.setAutoPlay = function(autoPlay) {
	this.tickEnabled = autoPlay;
}
p.play = function() { this.tickEnabled = true; this.getChildAt(0).gotoAndPlay(this.getTimelinePosition()) }
p.stop = function(ms) { if(ms) this.seek(ms); this.tickEnabled = false; }
p.seek = function(ms) { this.tickEnabled = true; this.getChildAt(0).gotoAndStop(lib.properties.fps * ms / 1000); }
p.getDuration = function() { return this.getChildAt(0).totalFrames / lib.properties.fps * 1000; }

p.getTimelinePosition = function() { return this.getChildAt(0).currentFrame / lib.properties.fps * 1000; }

an.bootcompsLoaded = an.bootcompsLoaded || [];
if(!an.bootstrapListeners) {
	an.bootstrapListeners=[];
}

an.bootstrapCallback=function(fnCallback) {
	an.bootstrapListeners.push(fnCallback);
	if(an.bootcompsLoaded.length > 0) {
		for(var i=0; i<an.bootcompsLoaded.length; ++i) {
			fnCallback(an.bootcompsLoaded[i]);
		}
	}
};

an.compositions = an.compositions || {};
an.compositions['50FC1612AB44944091A01156E58E0A1F'] = {
	getStage: function() { return exportRoot.getStage(); },
	getLibrary: function() { return lib; },
	getSpriteSheet: function() { return ss; },
	getImages: function() { return img; }
};

an.compositionLoaded = function(id) {
	an.bootcompsLoaded.push(id);
	for(var j=0; j<an.bootstrapListeners.length; j++) {
		an.bootstrapListeners[j](id);
	}
}

an.getComposition = function(id) {
	return an.compositions[id];
}



})(createjs = createjs||{}, AdobeAn = AdobeAn||{});
var createjs, AdobeAn;