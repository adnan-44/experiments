#include "Cube.h"
#include "Shape.h"

namespace uiuc{
 Cube::Cube(double width) : Shape(width);
 
 double Cube::getVolume() const{
  return getWidth() * getWidth() * getWidth();
 }
}
