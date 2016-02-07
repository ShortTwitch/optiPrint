var bests = {val : [{a:2, b:3, c:4}, {d:6,}], };

var temp = jQuery.extend({}, bests);

bests.val.push({g:5});


console.log(temp);

console.log(bests.val);
