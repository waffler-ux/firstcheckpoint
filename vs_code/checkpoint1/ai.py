import random
import sys

LEVEL_COUNT = 18
BLOCKS_PER_LEVEL = 3


def build_tower(levels=LEVEL_COUNT):
    return [[True] * BLOCKS_PER_LEVEL for _ in range(levels)]


def format_level(level_index, level):
    orientation = "H" if level_index % 2 == 0 else "V"
    blocks = " ".join("[?]" if present else "[ ]" for present in level)
    return f"{LEVEL_COUNT - level_index:2d} {orientation}: {blocks}"


def render_tower(tower):
    lines = [format_level(i, level) for i, level in enumerate(tower)]
    return "\n".join(lines)


def highest_full_level(tower):
    for i, level in enumerate(tower):
        if not all(level):
            return i
    return len(tower)


def valid_moves(tower):
    top_complete_index = highest_full_level(tower)
    moves = []
    for level_index in range(min(top_complete_index, len(tower))):
        level = tower[level_index]
        for block_index, present in enumerate(level):
            if present:
                moves.append((level_index, block_index))
    return moves


def collapse_chance(tower, row, block):
    level = tower[row]
    present_blocks = sum(level)
    missing_after = BLOCKS_PER_LEVEL - (present_blocks - 1)
    missing_count = BLOCKS_PER_LEVEL - present_blocks
    unsupported_blocks = sum(BLOCKS_PER_LEVEL - sum(tower[i]) for i in range(row))
    height_penalty = max(0, len(tower) - row - 5)
    chance = 0.01
    chance += 0.02 * height_penalty
    chance += 0.06 * missing_after
    chance += 0.02 * unsupported_blocks
    if row == 0:
        chance += 0.15
    return min(0.98, chance)


def apply_move(tower, row, block):
    tower[row][block] = False
    return collapse_chance(tower, row, block)


def choose_ai_move(tower):
    moves = valid_moves(tower)
    safe_moves = []
    best_score = 1.0
    for move in moves:
        score = collapse_chance(tower, move[0], move[1])
        if score < best_score:
            best_score = score
            safe_moves = [move]
        elif score == best_score:
            safe_moves.append(move)
    return random.choice(safe_moves) if safe_moves else None


def prompt_move(tower):
    moves = valid_moves(tower)
    if not moves:
        return None

    while True:
        user_input = input("Choose a block to remove as 'row block' (or q to quit): ").strip().lower()
        if user_input in {"q", "quit", "exit"}:
            print("Goodbye!")
            sys.exit(0)
        parts = user_input.split()
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("Enter two numbers like '5 2'.")
            continue

        row_choice = int(parts[0])
        block_choice = int(parts[1])
        row_index = LEVEL_COUNT - row_choice
        block_index = block_choice - 1

        if row_choice < 1 or row_choice > LEVEL_COUNT or block_choice < 1 or block_choice > BLOCKS_PER_LEVEL:
            print(f"Row must be 1-{LEVEL_COUNT} and block must be 1-{BLOCKS_PER_LEVEL}.")
            continue
        if row_index < 0 or row_index >= LEVEL_COUNT:
            print("That row is out of range.")
            continue
        if not tower[row_index][block_index]:
            print("That block is already removed.")
            continue
        if (row_index, block_index) not in moves:
            print("You may only remove a block from below the top complete level.")
            continue

        return row_index, block_index


def print_instructions():
    print("Welcome to CLI Jenga!")
    print("Remove a block from below the top fully complete level.")
    print("Blocks are shown as [�] for present and [ ] for missing.")
    print("Rows are numbered from bottom (1) to top (18).")
    print("Take turns with the AI. If the tower collapses, the last player loses.\n")


def main():
    tower = build_tower()
    print_instructions()
    player_turn = True

    while True:
        print(render_tower(tower))
        moves = valid_moves(tower)
        if not moves:
            print("No legal moves remain. The tower stands � it is a draw!")
            break

        if player_turn:
            move = prompt_move(tower)
            if move is None:
                print("No valid move selected. Game over.")
                break
            row, block = move
            chance = apply_move(tower, row, block)
            print(f"You removed block {block + 1} from row {LEVEL_COUNT - row}.")
            if random.random() < chance:
                print(render_tower(tower))
                print("The tower collapses! You lose.")
                break
        else:
            move = choose_ai_move(tower)
            if not move:
                print("AI cannot move. The tower stands.")
                break
            row, block = move
            chance = apply_move(tower, row, block)
            print(f"AI removes block {block + 1} from row {LEVEL_COUNT - row}.")
            if random.random() < chance:
                print(render_tower(tower))
                print("The tower collapses! AI loses � you win.")
                break

        player_turn = not player_turn
        print()


if __name__ == "__main__":
    main()
