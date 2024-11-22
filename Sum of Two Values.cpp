#include <iostream>
#include <map>

using namespace std;

int main() {
  int n, x;
  cin >> n >> x;

  map<int, int> positionOfValue;

  for (int i = 0; i < n; i++) {
    int element;
    cin >> element;
    
    if (positionOfValue.count(x - element)) {
      cout << i + 1 << " " << positionOfValue[x - element] << endl;
      return 0;
    } else positionOfValue[element] = i + 1;
  }

  cout << "IMPOSSIBLE" << endl;
  
  return 0;
}