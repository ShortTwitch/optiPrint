// Implementation for 'queue' that keeps the best
// #('num_best') elements at all times.
// Access ornts for the array
// Use push to put new things inside the queue
// (Only the top #('num_best') will be stored)

function BestQueue(num_best) {
    this.ornts = [];
    this.push = function (newOrnt) {
        if (ornts.length < num_best) {
            ornts.push(newOrnt);
            return;
        }
        for (var i = 0; i<ornts.length; i++) {
            var ornt = ornts[i];
            if (newOrnt.val > ornt.val) {
                ornts.splice(i, 0, newOrnt);
                break;
            }
        }
        ornts.sort(function(a, b) {return a.val - b.val});
        ornts = ornts.splice(0, num_best);
    }
}

// Generic implementation of 'zooming in' on orientations
// the calcValue function must take in 4 variables
// the list of faces, alpha, beta, and step values
// and return a 'score' for this orientation
// Levels is the number of times to 'zoom in'
// Returns the list of bests
function calcOrientations(calcValue, levels) {
    var queue = new BestQueue(3);
    queue.push({a: 0, b: 0, step: 360, val: 0});
    for(var i=0; i<levels; i++) {
        bests = queue.ornts;
        temps = []
        for(var k=0; k<bests.length; k++) {
            best = bests[k];
            step = best.step / 10;
            for(var iA=0; iA<10; iA++) {
                alpha = best.a + iA * step;
                for(var iB=0; iB<10; iB++) {
                    beta = best.b + iB * step;
                    val = calcValue(faces, alpha, beta, step);
                    temps.push({a: alpha, b: beta, step: step, val: val});
                }
            }
        }
        for(var k=0; k<temps.length; k++)
            queue.push(temps[k]);
    }
    return queue.ornts;
}