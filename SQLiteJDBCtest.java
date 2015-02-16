import java.sql.*;
import java.util.*;


public class DBConn
{

	public DBConn()
	{
		try
		{
			Statement stmt = null;
			Class.forName("org.sqlite.JDBC"); 
			c = DriverManager.getConnection("jdbc:sqlite:schedule.db");
			System.out.println("Opened database succesfully");
		}
			catch (Exception e)
		{
			System.err.println( e.getClass().getName() + ": " + e.getMessage() );
			System.exit(0);
		}
	}


	/*  */
	public static ArrayList<Integer> getResults()
	{
		ArrayList<Integer> results = new ArrayList<Integer>(); 				// set up results arraylist

		cmd = c.createStatement();
		ResultSet rs = cmd.executeQuery("Select * from schedule; "); 	// sql command to iterate through schedule table

		while ( rs.next() )
		{
			String result = rs.getString("result"); 					// result holds either 'A' or 'H' or 'NA' based on who has won
			String homeTeam = rs.getString("home"); 					// home team holds the name of the home team
			String extraQual = rs.getString("extra"); 					// extra holds whether or not the game went to SO or OT
			
			int num = 0;
			if (result.equals("H"))
			{
				num = (homeTeam.equals("Red Wings")) ? 2 : -1; 		// stores a win for the red wings as a 2, OT/SO win as 1, loss as -1
			}
			else if (result.equals("A"))
			{
				num =(homeTeam.equals("Red Wings")) ? -1 : 2; 		// stores a win for the red wings as a 2, OT/SO win as 1, loss as -1
			}
			// if it is NA it skips the if - elseif statement

			// if the red wings lost but it went to OT or SO
			if (num == -1 && (extraQual.equals("OT") || extraQual.equals("SO")))
				num = 1;
			

			results.add(num);


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
		ArrayList<Integer> results = new ArrayList<Integer>(getResults());
		int points = 0;
		int wins = 0;
		int losses = 0;
		int extra = 0;
		for (int element : results)
		{
			if (element > 0)
				points += element;

			if (element == -1)
				losses += 1;
			else if (element == 2)
				wins += 1;
			else if (element == 1)
				extra += 1;
		}
		System.out.println("Total games: " + results.size());
		System.out.println("Current record: " + wins + "-" + losses + "-" + extra);
		System.out.println("Current Points: " + points);
	}
}