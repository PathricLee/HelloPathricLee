#include <iostream>
#include <vector>
#include <sstream>

void lprint(std::vector<std::string> &words);

void read2pipe() {
    // std::in

    std::string line;
    while(std::getline(std::cin, line)) {
        std::istringstream s(line);
        std::string word;
        std::vector<std::string> words;
        while(s >> word) {
            words.push_back(word);
        }
        if (words.size() != 2) {
            lprint(words);
        }
    }
}

void lprint(std::vector<std::string> &words) {
    for (std::vector<std::string>::iterator iter = words.begin();
            iter != words.end(); iter++) {
        std::cout << (*iter) << "\t";
    }
    std::cout << std::endl;
}

int main() {
    read2pipe();
    return 0;
}
