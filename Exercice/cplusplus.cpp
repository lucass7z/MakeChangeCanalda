#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>

struct CoinQuantity {
    double coin;
    int quantity;
};

std::vector<CoinQuantity> calculate(double m, const std::vector<double>& L) {
    std::vector<CoinQuantity> S_Fifo;
    for (double coin : L) {
        int count = static_cast<int>(m / coin);
        S_Fifo.push_back({coin, count});
        m -= coin * count;
        m = std::round(m * 100.0) / 100.0;
    }
    return S_Fifo;
}

void printSolution(const std::vector<CoinQuantity>& solution) {
    std::cout << std::setw(10) << "Coin" << std::setw(10) << "Quantity" << std::endl;
    for (const auto& cq : solution) {
        std::cout << std::setw(10) << cq.coin << std::setw(10) << cq.quantity << std::endl;
    }
}

int main() {
    double m = 12.35;
    std::vector<double> L;
    std::ifstream file("L.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::stringstream ss(line);
            std::string num;
            while (std::getline(ss, num, ',')) {
                L.push_back(std::stod(num));
            }
        }
        file.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
        return 1;
    }
    //Start Timer
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<CoinQuantity> solution = calculate(m, L);
    //End Timer
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Elapsed time: " << elapsed.count() << "s" << std::endl;
    printSolution(solution);
    return 0;
}