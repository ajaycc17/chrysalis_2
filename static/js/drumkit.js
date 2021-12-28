var nDrums = document.querySelectorAll(".drum").length;

for (var i = 0; i < nDrums; i++) {
    document
        .querySelectorAll(".drum")
        [i].addEventListener("click", function () {
            var buttonKey = this.innerHTML;
            beatDrum(buttonKey);
            btnAnim(buttonKey);
        });
}

document.addEventListener("keydown", function (event) {
    beatDrum(event.key);
    btnAnim(event.key);
});

function beatDrum(key) {
    switch (key) {
        case "w":
            var audio = new Audio("/static/sounds/tom-1.mp3");
            break;
        case "a":
            var audio = new Audio("/static/sounds/tom-2.mp3");
            break;
        case "s":
            var audio = new Audio("/static/sounds/tom-3.mp3");
            break;
        case "d":
            var audio = new Audio("/static/sounds/tom-4.mp3");
            break;
        case "j":
            var audio = new Audio("/static/sounds/snare.mp3");
            break;
        case "k":
            var audio = new Audio("/static/sounds/crash.mp3");
            break;
        case "l":
            var audio = new Audio("/static/sounds/kick-bass.mp3");
            break;

        default:
            console.log("button not defined");
            break;
    }
    audio.play();
}

function btnAnim(key) {
    var btnClass = `.${key}`;
    document.querySelector(btnClass).classList.add("pressed");

    setTimeout(() => {
        document.querySelector(btnClass).classList.remove("pressed");
    }, 100);
}
