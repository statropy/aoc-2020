//day15.cpp
#include <unordered_map>
#include <iostream>
#include <list>
#include <gtest/gtest.h>

int number_game(const std::list<int> & initial, int stop=2020)
{
    std::unordered_map<int, int> numbers;
    int last = 0;
    int turn = 1;
    for (int n : initial) {
        numbers.insert({n,turn++});
    }
    for(; turn<stop; turn++) {
        int v = numbers[last];
        numbers[last] = turn;
        last = (v == 0) ? 0 : turn - v;
    }
    return last;
}

#ifdef GTEST
TEST(NumberGameTest, Part1) {
    ASSERT_EQ(436, number_game({0,3,6}));
    ASSERT_EQ(1, number_game({1,3,2}));
    ASSERT_EQ(10, number_game({2,1,3}));
    ASSERT_EQ(27, number_game({1,2,3}));
    ASSERT_EQ(78, number_game({2,3,1}));
    ASSERT_EQ(438, number_game({3,2,1}));
    ASSERT_EQ(1836, number_game({3,1,2}));
    ASSERT_EQ(387, number_game({14,1,17,0,3,20}));
}

TEST(NumberGameTest, Part2) {
    int stop = 30000000;
    ASSERT_EQ(175594, number_game({0,3,6},stop));
    ASSERT_EQ(2578, number_game({1,3,2},stop));
    ASSERT_EQ(3544142, number_game({2,1,3},stop));
    ASSERT_EQ(261214, number_game({1,2,3},stop));
    ASSERT_EQ(6895259, number_game({2,3,1},stop));
    ASSERT_EQ(18, number_game({3,2,1},stop));
    ASSERT_EQ(362, number_game({3,1,2},stop));
    ASSERT_EQ(6428, number_game({14,1,17,0,3,20},stop));
}

#else

int main()
{
    std::cout << number_game({14,1,17,0,3,20}) << "\n"
              << number_game({14,1,17,0,3,20}, 30000000) << "\n";
    return 0;
}
#endif
