#include <iostream>
#include <sqlite3.h>

using std::cerr;
using std::cout;
using std::endl;

int main()
{
	sqlite3 *db;
	char *sql; // commands for sql
	int rc;

	rc = sqlite3_open("schedule.db", &db);

	if ( rc ){
		cerr << "Can't open database: " << sqlite3_errmsg(db) << endl;
	}
	else
	{
		cerr << "Opened database successfully" << endl;
	}

	sql = "SELECT * from "

	sqlite3_close(db);

}