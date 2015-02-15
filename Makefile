CXX = clang++
CXXFLAGS = -std=c++1y -stdlib=libc++ -g -O0 -Wall -Wextra -Werror -pedantic 
LDFLAGS = -std=c++1y -stdlib=libc++ -lc++abi -l sqlite3

OBJS = test.o

redwings: $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o redwings

test.o:
	$(CXX) $(CXXFLAGS) -c test.cpp


clean:
	rm *.o redwings