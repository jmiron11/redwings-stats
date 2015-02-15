#include <iostream>
#include <sqlite3.h>

using std::cerr;
using std::cout;
using std::endl;

int callback(void *data, int argc, char **argv, char **colName)
{
	int i;
	if (data) cout << (const char*)data;
	for(i=0; i<argc; i++)
	{
		cout << colName[i] << " = " << argv[i] << endl;
	}
	printf("\n");
	return 0;
}

int main()
{
	sqlite3 *db;
	int rc;

	rc = sqlite3_open("schedule.db", &db);

	if ( rc ){
		cerr << "Can't open database: " << sqlite3_errmsg(db) << endl;
	}
	else
	{
		cerr << "Opened database successfully" << endl;
	}

	char *sql = (char *)("SELECT * from schedule");
	char *errMsg = nullptr;
	rc = sqlite3_exec(db, sql, callback, nullptr, &errMsg);

	sqlite3_close(db);

}