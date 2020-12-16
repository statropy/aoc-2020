//day15.cpp
#include <unordered_map>
#include <map>
#include <iostream>
#include <list>

int number_linear(const std::list<int> & initial, int stop=2020)
{
    int *numbers = (int*)malloc(sizeof(int)*(stop));
    int last = 0;
    int turn = 1;

    if(!numbers) {return -1;}

    memset(numbers, 0, sizeof(int)*stop);

    for (int n : initial) {
        numbers[n] = turn++;
    }

    for(; turn<stop; turn++) {
        int v = numbers[last];
        numbers[last] = turn;
        last = (v == 0) ? 0 : turn - v;
    }

    free(numbers);

    return last;
}

int number_game(const std::list<int> & initial, int stop=2020)
{
    std::unordered_map<int, int> numbers;
    int last = 0;
    int turn = 1;

    numbers.reserve(stop>>1);

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

int number_iterator(const std::list<int> & initial, int stop=2020)
{
    std::unordered_map<int, int> numbers;
    int last = 0;
    int turn = 1;

    numbers.reserve(stop>>1);

    for (int n : initial) {
        numbers.insert({n,turn++});
    }

    for(; turn<stop; turn++) {
        std::unordered_map<int, int>::iterator it = numbers.find(last);
        if(it == numbers.end()) {
            numbers.insert({last,turn});
            last = 0;
        } else {
            last = turn - it->second;
            it->second = turn;
        }
    }
    return last;
}


int number_map(const std::list<int> & initial, int stop=2020)
{
    std::map<int, int> numbers;
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
#include <gtest/gtest.h>
TEST(NumberGameTest, Part1) {
    ASSERT_EQ(436, number_game({0,3,6}));
    ASSERT_EQ(1, number_game({1,3,2}));
    ASSERT_EQ(10, number_game({2,1,3}));
    ASSERT_EQ(27, number_game({1,2,3}));
    ASSERT_EQ(78, number_game({2,3,1}));
    ASSERT_EQ(438, number_game({3,2,1}));
    ASSERT_EQ(1836, number_game({3,1,2}));
    ASSERT_EQ(387, number_game({14,1,17,0,3,20}));
    ASSERT_EQ(4, number_iterator({0,3,6},9));
    ASSERT_EQ(436, number_iterator({0,3,6}));
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

TEST(NumberGameTest, Part2It) {
    int stop = 30000000;
    ASSERT_EQ(175594, number_iterator({0,3,6},stop));
    ASSERT_EQ(2578, number_iterator({1,3,2},stop));
    ASSERT_EQ(3544142, number_iterator({2,1,3},stop));
    ASSERT_EQ(261214, number_iterator({1,2,3},stop));
    ASSERT_EQ(6895259, number_iterator({2,3,1},stop));
    ASSERT_EQ(18, number_iterator({3,2,1},stop));
    ASSERT_EQ(362, number_iterator({3,1,2},stop));
    ASSERT_EQ(6428, number_iterator({14,1,17,0,3,20},stop));
}

TEST(NumberGameTest, Part2Linear) {
    int stop = 30000000;
    ASSERT_EQ(175594, number_linear({0,3,6},stop));
    ASSERT_EQ(2578, number_linear({1,3,2},stop));
    ASSERT_EQ(3544142, number_linear({2,1,3},stop));
    ASSERT_EQ(261214, number_linear({1,2,3},stop));
    ASSERT_EQ(6895259, number_linear({2,3,1},stop));
    ASSERT_EQ(18, number_linear({3,2,1},stop));
    ASSERT_EQ(362, number_linear({3,1,2},stop));
    ASSERT_EQ(6428, number_linear({14,1,17,0,3,20},stop));
}

// TEST(NumberGameTest, Part2a) {
//     int stop = 30000000;
//     ASSERT_EQ(175594, number_game({0,3,6},stop));
// }
// TEST(NumberGameTest, Part2b) {
//     int stop = 30000000;
//     ASSERT_EQ(2578, number_game({1,3,2},stop));
// }
// TEST(NumberGameTest, Part2c) {
//     int stop = 30000000;
//     ASSERT_EQ(3544142, number_game({2,1,3},stop));
// }
// TEST(NumberGameTest, Part2d) {
//     int stop = 30000000;
//     ASSERT_EQ(261214, number_game({1,2,3},stop));
// }
// TEST(NumberGameTest, Part2e) {
//     int stop = 30000000;
//     ASSERT_EQ(6895259, number_game({2,3,1},stop));
// }
// TEST(NumberGameTest, Part2f) {
//     int stop = 30000000;
//     ASSERT_EQ(18, number_game({3,2,1},stop));
// }
// TEST(NumberGameTest, Part2g) {
//     int stop = 30000000;
//     ASSERT_EQ(362, number_game({3,1,2},stop));
// }
// TEST(NumberGameTest, Part2h) {
//     int stop = 30000000;
//     ASSERT_EQ(6428, number_game({14,1,17,0,3,20},stop));
// }

// TEST(NumberGameTest, Part1hL) {
//     ASSERT_EQ(387, number_linear({14,1,17,0,3,20}));
// }
// TEST(NumberGameTest, Part2hL) {
//     int stop = 30000000;
//     ASSERT_EQ(6428, number_linear({14,1,17,0,3,20},stop));
// }

// TEST(NumberGameTest, Map1) {
//     ASSERT_EQ(436, number_map({0,3,6}));
//     ASSERT_EQ(1, number_map({1,3,2}));
//     ASSERT_EQ(10, number_map({2,1,3}));
//     ASSERT_EQ(27, number_map({1,2,3}));
//     ASSERT_EQ(78, number_map({2,3,1}));
//     ASSERT_EQ(438, number_map({3,2,1}));
//     ASSERT_EQ(1836, number_map({3,1,2}));
//     ASSERT_EQ(387, number_map({14,1,17,0,3,20}));
// }

// TEST(NumberGameTest, Map2) {
//     int stop = 30000000;
//     ASSERT_EQ(175594, number_map({0,3,6},stop));
//     ASSERT_EQ(2578, number_map({1,3,2},stop));
//     ASSERT_EQ(3544142, number_map({2,1,3},stop));
//     ASSERT_EQ(261214, number_map({1,2,3},stop));
//     ASSERT_EQ(6895259, number_map({2,3,1},stop));
//     ASSERT_EQ(18, number_map({3,2,1},stop));
//     ASSERT_EQ(362, number_map({3,1,2},stop));
//     ASSERT_EQ(6428, number_map({14,1,17,0,3,20},stop));
// }

#else

int main()
{
    std::cout << number_linear({14,1,17,0,3,20}) << std::endl
              << number_linear({14,1,17,0,3,20}, 30000000) << std::endl;
    return 0;
}
#endif
