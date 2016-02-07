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

var calcOrientations = function(calcValue, levels) {
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
};


var app = angular.module('slider', []);

app.controller('sliderController', function($scope) {
   
    var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var index = 0;
    $scope.vals = [];
    
    $scope.increase = function(val) {
        val.val += 1;
    };
    
    $scope.decrease = function(val) {
        val.val -= 1;
    };
    
    $scope.remove = function(val) {
        var index = $scope.vals.indexOf(val);
        if (index > -1)
            $scope.vals.splice(index, 1);
    };
    
    $scope.addVal = function () {
        if (index < 26) {
            $scope.vals.push({name: letters[index], val: 0});
            index += 1;
        }
    };
    
});