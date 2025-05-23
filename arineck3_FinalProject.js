function areaSolving() {
  var shape = "";
  var length = 0;
  var length2 = 0;
  var width = 0;
  var height = 0;
  var radius = 0;
  var area = 0;
  
  shape = prompt("Enter the name of the shape.");
  
    if (shape == "square" || shape == "Square") {
      length = Number(prompt("Please enter the length of the square's sides."));
      area = length * length;
      document.write("Length: " + length + "<br><br><b>Area: " + area + "</b><br><br>Thank you for participating!");
    } else if (shape == "rectangle" || shape == "Rectangle" || shape == "parallelogram" || shape == "Parallelogram") {
      length = Number(prompt("Please enter the length of the " + shape + "."));
      width = Number(prompt("Please enter the width of the " + shape + "."));
      area = length * width;
      document.write("Length: " + length + "<br><br>Width: " + width + "<br><br><b>Area: " + area + "</b><br><br>Thank you for participating!");
    } else if (shape == "circle" || shape == "Circle") {
      radius = Number(prompt("Please enter the radius of the circle."));
      area = (Math.PI * (radius * radius)).toFixed(2);
      document.write("Radius: " + radius + "<br><br><b>Area: " + area + "</b><br><br>Thank you for participating!");
    } else if (shape == "triangle" || shape == "Triangle") {
      length = Number(prompt("Please enter the length of the triangle."));
      height = Number(prompt("Please enter the height of the triangle."));
      area = length * height / 2;
      document.write("Length: " + length + "<br><br>Height: " + height + "<br><br><b>Area: " + area + "</b><br><br>Thank you for participating!");
    } else if (shape == "trapezoid" || shape == "Trapezoid") {
      length = Number(prompt("Please enter the first length of the trapezoid."));
      length2 = Number(prompt("Please enter the second length of the trapezoid."));
      height = Number(prompt("Please enter the height of the trapezoid."));
      area = ((length * length2) * height) / 2;
      document.write("First Length: " + length + "<br><br>Second Length: " + length2 + "<br><br>Height: " + height
        + "<br><br><b>Area: " + area + "</b><br><br>Thank you for participating!");
    } else {
      document.write("\"" + shape + "\" is not a valid shape.  Please enter a shape.");
    }
}
  

areaSolving();