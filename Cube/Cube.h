#pragma once
#include "Shape.h"

namespace uiuc{
 Class Cube : public Shape{
  public:
   Cube(double width);
   double getVolume() const;

  };
}
