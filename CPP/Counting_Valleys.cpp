#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
bool m = true;
int count=0, v=0;
for (int i=0;i<s.size();i++){
    if (s[i]=='U')
    count++;
    else 
    count--;
    
    if(count<0&&m){
        m= false;
        v++;
    }
    if(count>=0)
    m=true; 

}
return v;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
