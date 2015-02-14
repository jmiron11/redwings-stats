CXX = clang++
CXXFLAGS = -std=c++1y -g -O0 -Wall -Wextra -Werror -pedantic 
LDFLAGS = -std=c++1y -l sqlite3

OBJS = accessinfo.o

redwings: $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o redwings

accessinfo.o:
	$(CXX) $(CXXFLAGS) -c accessinfo.cpp


clean:
	rm *.o redwings