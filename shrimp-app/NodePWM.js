var rpio = require('rpio');

/*
 * Set the initial state to low.  The state is set prior to the pin becoming
 * active, so is safe for devices which require a stable setup.
 */
var PWM_PIN_RED = 11
var PWM_PIN_GREEN = 13
var PWM_PIN_BLUE = 15
rpio.open(PWM_PIN_RED, rpio.OUTPUT, rpio.LOW);
rpio.open(PWM_PIN_GREEN, rpio.OUTPUT, rpio.LOW);
rpio.open(PWM_PIN_BLUE, rpio.OUTPUT, rpio.LOW);
/*
 * The sleep functions block, but rarely in these simple programs does one care
 * about that.  Use a setInterval()/setTimeout() loop instead if it matters.
 */
for (var i = 0; i < 5; i++) {
        /* On for 1 second */
        rpio.write(PWM_PIN_RED, rpio.HIGH);
        rpio.write(PWM_PIN_GREEN, rpio.HIGH);
        rpio.write(PWM_PIN_BLUE, rpio.HIGH);
        rpio.sleep(1);

        /* Off for half a second (500ms) */
        rpio.write(PWM_PIN_RED, rpio.LOW);
        rpio.write(PWM_PIN_GREEN, rpio.LOW);
        rpio.write(PWM_PIN_BLUE, rpio.LOW);
        rpio.sleep(1);
}