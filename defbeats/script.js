
function change_screens1() {
	var loading = 0;
	var id = setInterval(frame, 64);
	function frame() {
		if(loading == 30) {
			clearInterval(id);
			window.open('equalizers/equalizer1.html', '_self');
		} else {
			//document.getElementById("spinner").style.visibility = "visible";
			loading = loading + 1;
			if(loading == 20) {
				style.animation = 'fadeout 1s ease';
			}
		}
	}

	frame();
};

function change_screens2() {

	var loading = 0;
	var id = setInterval(frame, 64);
	function frame() {
		if(loading == 30) {
			clearInterval(id);
			window.open('equalizers/equalizer2.html', '_self');
		} else {
			//document.getElementById("spinner").style.visibility = "visible";
			loading = loading + 1;
			if(loading == 20) {
				style.animation = 'fadeout 1s ease';
			}
		}
	}

	frame();
};

function change_screens3() {

	var loading = 0;
	var id = setInterval(frame, 64);
	function frame() {
		if(loading == 30) {
			clearInterval(id);
			window.open('equalizers/equalizer3.html', '_self');
		} else {
			//document.getElementById("spinner").style.visibility = "visible";
			loading = loading + 1;
			if(loading == 20) {
				style.animation = 'fadeout 1s ease';
			}
		}
	}

	frame();
};

function change_screens4() {

	var loading = 0;
	var id = setInterval(frame, 64);
	function frame() {
		if(loading == 30) {
			clearInterval(id);
			window.open('equalizers/equalizer4.html', '_self');
		} else {
			//document.getElementById("spinner").style.visibility = "visible";
			loading = loading + 1;
			if(loading == 20) {
				style.animation = 'fadeout 1s ease';
			}
		}
	}

	frame();
};

function change_screens5() {

	var loading = 0;
	var id = setInterval(frame, 64);
	function frame() {
		if(loading == 30) {
			clearInterval(id);
			window.open('equalizers/equalizer5.html', '_self');
		} else {
			//document.getElementById("spinner").style.visibility = "visible";
			loading = loading + 1;
			if(loading == 20) {
				style.animation = 'fadeout 1s ease';
			}
		}
	}

	frame();
};
