import argparse
from sourcebot.ingestor import DocumentIngestor
from sourcebot.chatbot import ChatBot


def main():
    parser = argparse.ArgumentParser(description="SourceBot CLI")
    parser.add_argument("--ingest", help="Path or URL to documents", default=None)
    parser.add_argument("--chat", action="store_true", help="Start chatbot")

    args = parser.parse_args()

    if args.ingest:
        print("📥 Ingesting documents...")
        ingestor = DocumentIngestor(args.ingest)
        ingestor.process()
        ingestor.save()
        print("✅ Ingestion complete.")

    if args.chat:
        print("🤖 Starting chatbot...")
        bot = ChatBot()
        while True:
            query = input("\n🔍 Ask a question (or 'exit'): ")
            if query.lower() in ["exit", "quit"]:
                break
            answer = bot.ask(query)
            print(f"\n🧠 Answer:\n{answer}\n")


if __name__ == "__main__":
    main()
