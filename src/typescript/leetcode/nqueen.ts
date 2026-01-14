/** 
    place n Queen in a nxn board,such that no queen is under attack.
    using backtracking.
*/
export function solveNQueens(n: number) {
  const solutions: number[][] = [];
  const board: number[] = [];

  for (let i = 0; i < n; i++) {
    board.push(-1);
  }

  function isSafe(row: number, column: number) {
    // check all previous rows
    for (let prev_row in Array.from(Array(row).keys())) {
      let prev_column = board[prev_row];

      if (column === prev_column) {
        return false;
      }
      if (Math.abs(column - prev_column) === Math.abs(row - Number(prev_row))) {
        return false;
      }
    }
    return true;
  }

  // loop through rows
  function backtrack(row: number) {
    // record solution if found
    if (row === n) {
      if (board.length === n) solutions.push([...board]);
      return;
    }
    // go through each column & check if its safe to place a queen

    for (let column in [...Array(n).keys()]) {
      if (isSafe(row, Number(column))) {
        // place a queen in that column
        board[row] = Number(column);
        // move to next row
        backtrack(row + 1);
        // go back if you cant find a place
        board[row] = -1;
      }
    }
  }
  backtrack(0);

  function showBoard(solution: number[]) {
    let board = "";

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (j === solution[i]) {
          board = board + "Q ";
        } else {
          board = board + ". ";
        }
      }
      board += "\n";
    }
    console.log(board);
  }
  console.log(solutions);

  if (solutions.length > 0) {
    solutions.forEach((solution, index) => {
      console.log(`------- solutions #${index}-------`);
      showBoard(solution);
    });
  }

  console.log("Invalid Input");
}
