# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: IdeaVault
import argparse

def main():
    parser = argparse.ArgumentParser(description='IdeaVault CLI')
    sub = parser.add_subparsers(dest='command', required=True)

    # create
    p_create = sub.add_parser('create', help='create idea')
    p_create.add_argument('--title', required=True)
    p_create.add_argument('--category', default='uncategorized')
    p_create.add_argument('--score', type=int, default=0)
    p_create.add_argument('--status', default='idea')

    # read
    p_read = sub.add_parser('read', help='read idea')
    p_read.add_argument('--id', type=int, required=True)

    # update
    p_update = sub.add_parser('update', help='update idea')
    p_update.add_argument('--id', type=int, required=True)
    p_update.add_argument('--title', default=None)
    p_update.add_argument('--category', default=None)
    p_update.add_argument('--score', type=int, default=None)
    p_update.add_argument('--status', default=None)

    # list
    sub.add_parser('list', help='list all ideas')

    args = parser.parse_args()

    ideas = load_ideas()

    if args.command == 'create':
        ideas.append(Idea(
            id=len(ideas)+1,
            title=args.title,
            category=args.category,
            score=args.score,
            status=args.status,
        ))
        save_ideas(ideas)
        print(f'Created idea #{len(ideas)}: {args.title}')

    elif args.command == 'read':
        if 1 <= args.id <= len(ideas):
            print(ideas[args.id - 1])
        else:
            print('Idea not found.')

    elif args.command == 'update':
        if 1 <= args.id <= len(ideas):
            idea = ideas[args.id - 1]
            if args.title: idea.title = args.title
            if args.category: idea.category = args.category
            if args.score is not None: idea.score = args.score
            if args.status: idea.status = args.status
            save_ideas(ideas)
            print(f'Updated idea #{args.id}')
        else:
            print('Idea not found.')

    elif args.command == 'list':
        if ideas:
            for i in ideas: print(i)
        else: print('No ideas yet.')

if __name__ == '__main__':
    main()
