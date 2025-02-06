#include <x86intrin.h>

int main() {
  unsigned int rdtscp_buf;
  unsigned long int result = __rdtscp(&rdtscp_buf);
  return result % 10;
}
