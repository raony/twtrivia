function Timer(initialTime) {
  this.initial = initialTime || 0;
	this.startTime = 0;
	this.endTime = null;

	this.start = function() {
    this.endTime = null;
		this.startTime = new Date().getTime();
	};

	this.stop = function() {
		this.endTime = new Date().getTime();
	};

  this.current_elapsed = function() {
    if( this.startTime == 0) { return 0; }
	end = Date.now();
    if( this.endTime ) { end = this.endTime; }

    return end - this.startTime + this.initial;
  };

  this.elapsedSeconds = function() {
    return this.current_elapsed() / 1000;
  };

  this.formatMilliseconds = function() {
    var milliseconds = this.current_elapsed();
    var m = Math.floor( milliseconds/1000/60 );
    var s = Math.floor( (milliseconds/1000) % 60 );
    var ms = milliseconds - (s*1000) - (m*60*1000);

    s = zeroPad(s, 2);
    ms = zeroPad(ms, 3);

    return m + ":" + s + ":" + ms;

  };

  function zeroPad( num, size) {
    var s = "000" + num;
    return s.substr(s.length - size);
  }

}
