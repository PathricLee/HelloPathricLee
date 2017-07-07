// 二进制读写文件

#include <iostream>
#include <fstream>

void print_bi(unsigned char a) {
    for (int i = 7; i >= 0; i--) {
        std::cout << ((a >> i) & 1);
    }
    std::cout << std::endl;
}

void test() {
    unsigned char chr1 = 123;
    unsigned char chr2 = 153;
    unsigned char chr3 = (unsigned char)(chr1 ^ chr2);
    std::cout << chr1 << std::endl;
    std::cout << chr2 << std::endl;
    std::cout << (int)chr3 << std::endl;
    print_bi(chr1);
    print_bi(chr2);
    print_bi(chr3);
}

void readfile() {
    unsigned char key = 9;
    std::string line;
    bool flag = true;
    while (std::getline(std::cin, line)) {
        std::string::iterator it = line.begin();

        if ((char)(*it)  != 'r') {
            std::cout << line << std::endl;
            continue;
        }

        for (; it != line.end(); it++) {
            unsigned char chr = (unsigned char)(*it);
            unsigned char chr3 = (unsigned char)(key ^ chr);
            if (chr3 != '\n') {
                std::cout << chr3;
            }
        } 
        std::cout << std::endl;
    }
}

int main() {
    readfile();
    return 0;
}
