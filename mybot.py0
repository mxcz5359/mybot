from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

BOT_TOKEN = "8146979262:AAF0DbqC1h2X7DEbeMXec23TPQOwULJed8U"

async def start_command(update: Update, context: CallbackContext) -> None:
    """处理 /start 命令，显示用户ID"""
    user_id = update.message.from_user.id
    await update.message.reply_text(f"你的用户ID是: {user_id}")

async def profile_command(update: Update, context: CallbackContext) -> None:
    """处理 /profile 命令，显示机器人Token"""
    await update.message.reply_text(f"机器人API Token: {BOT_TOKEN}")

async def help_command(update: Update, context: CallbackContext) -> None:
    """处理 /help 命令"""
    help_text = """
    可用命令：
    /start - 显示你的用户ID
    /profile - 显示机器人API Token
    """
    await update.message.reply_text(help_text)

def main() -> None:
    """启动机器人（适用于 python-telegram-bot 20+）"""
    app = Application.builder().token(BOT_TOKEN).build()

    # 注册命令处理器
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("profile", profile_command))
    app.add_handler(CommandHandler("help", help_command))

    # 启动轮询
    app.run_polling()

if __name__ == '__main__':
    main()
