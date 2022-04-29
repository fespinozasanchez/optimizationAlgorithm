#include <iostream>
#include <list>
using namespace std;


bool IsEmpty(list<int> lists) {
  if (lists.empty()) {
    return true;
  } else {
    return false;
  }
}

int main() {
  list<int> array;
  //añadir un numero a la lista por consola
  int num;
  cin >> num;
  array.push_back(num);
  //añadir otro numero a la lista por consola
  cin >> num;
  array.push_back(num);
  //añadir otro numero a la lista por consola
  cin >> num;
  array.push_back(num);
  //imprimir la lista
  cout << "Lista: ";
  for (int i = 0; i < array.size(); i++) {
    cout << array.front() << " ";
    array.pop_front();
  }
  cout << endl;
  //imprimir si la lista esta vacia
  cout << "Lista vacia: " << IsEmpty(array) << endl;
  return 0;
}
