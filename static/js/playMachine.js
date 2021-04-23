
function onDragStart (source, piece, position, orientation) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // only pick up pieces for the side to move
  if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
    return false
  }
}

//make an ajax request to /move_response/task_id
//if the machine came up with a move, play it.
//else schedule another ajax request
function pollMachine (response) {
    function recurse(){
        pollMachine(response);
    }
    $.ajax({
          type:"GET",
          url:"/move_response/"+response['task_id'],
          success:function(resp){
              if(resp['ready']){
                   document.open();
                   document.write(resp['newBoard']);
                   document.close();  
                   }
              else{
                   setTimeout(recurse,1000);
                   }
              }
          });
}
function onDrop (source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })
  
  // illegal move
  if (move === null) return 'snapback'
 
  updateStatus()
  console.log("Hello!");
  $.ajax({
      type:"POST",
      url:"/move",
      dataType:"json",
      data:{
        'fen_string':game.fen()
      },
      success:pollMachine
  });
}
// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
  board.position(game.fen())
}

function updateStatus () {
  var status = ''

  var moveColor = 'White'
  if (game.turn() === 'b') {
    moveColor = 'Black'
  }

  // checkmate?
  if (game.in_checkmate()) {
    status = 'Game over, ' + moveColor + ' is in checkmate.'
  }

  // draw?
  else if (game.in_draw()) {
    status = 'Game over, drawn position'
  }

  // game still on
  else {
    status = moveColor + ' to move'

    // check?
    if (game.in_check()) {
      status += ', ' + moveColor + ' is in check'
    }
  }

  $status.html(status)
  $fen.html(game.fen())
  $pgn.html(game.pgn())
}


