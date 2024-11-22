#include <iostream>
#include <bitset>

using namespace std;

int main() {
  long long int n;
  cin >> n;

  for (int i = 0; i < 1 << n; i++) {
    long long int val = i ^ (i >> 1);
    bitset<32> f(val);

    string a = f.to_string();

    for (int i = 32 - n; i < 32; i++) cout << a[i];
    cout << endl;
  }

  return 0;
}