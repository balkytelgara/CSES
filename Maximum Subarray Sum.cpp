#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  long long x[n];

  for (int i = 0; i < n; i++) cin >> x[i];

  long long best = -1e18;
  long long past = 0;

  for (int i = 0; i < n; i++) {
    if (past + x[i] >= x[i])
      past += x[i];
    else
      past = x[i];

    best = max(best, past);
  }

  cout << best << endl;
  return 0;
}