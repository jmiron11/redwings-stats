import java.sql.*;
import java.util.*;


public class SQLiteJDBC
{

	/*  */
	public static ArrayList<Integer> getResults()
	{
		ArrayList<Integer> results = new ArrayList<Integer>(); 				// set up results arraylist
		Connection c = null;
		Statement cmd = null;
		try
		{
			Class.forName("org.sqlite.JDBC"); 
			c = DriverManager.getConnection("jdbc:sqlite:schedule.db");
			System.out.println("Opened database succesfully");

			cmd = c.createStatement();
			ResultSet rs = cmd.executeQuery("Select * from schedule; "); 	// sql command to iterate through schedule table

			while ( rs.next() )
			{
				String result = rs.getString("result"); 					// result holds either 'A' or 'H' or 'NA' based on who has won
				String homeTeam = rs.getString("home"); 					// home team holds the name of the home team
				String extraQual = rs.getString("extra"); 					// extra holds whether or not the game went to SO or OT
				if (extraQual.equals("OT") || extraQual.equals("SO"))
				{
					results.add(1);
				}
				else
				{
					if (result.equals("H"))
					{
						int num = (result.equals("Red Wings")) ? 2 : -1; 		// stores a win for the red wings as a 2, OT/SO win as 1, loss as -1
						results.add(num);
					}
					else if (result.equals("A"))
					{
						int num =(result.equals("Red Wings")) ? -1 : 2; 		// stores a win for the red wings as a 2, OT/SO win as 1, loss as -1
						results.add(num);
					}
					else
					{
						results.add(0); 							 			// stores a game not played yet as 0
					}
				}

			}
			rs.close();
			cmd.close();
			c.close();
		}
		catch (Exception e)
		{
			System.err.println( e.getClass().getName() + ": " + e.getMessage() );
			System.exit(0);
		}
		System.out.println("Operation done succesfully");
		return results;
	}

	public static void main( String args[] )
	{
		ArrayList<Integer> results = new ArrayList<Integer>();
		results = getResults();
		int points = 0;
		for (int element : results)
			if (element > 0)
			{
				points += element;
			}

		System.out.println("Total games: " + results.size());
		System.out.println("Current Points: " + points);
	}
}