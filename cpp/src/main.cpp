#include <iostream>
#include <string>

std::string greet(const std::string& name) {
    return "Hello, " + name + "! Let's prototype some C++ route optimizers.";
}

int main(int argc, char** argv) {
    std::string name = "traveler";
    if (argc > 1) {
        name = argv[1];
    }

    std::cout << greet(name) << std::endl;
    return 0;
}
