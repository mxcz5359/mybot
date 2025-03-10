import os
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# 从环境变量中读取 BOT_TOKEN
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("错误：请设置 BOT_TOKEN 环境变量！")
    exit()

ALLOWED_USER_IDS = [
   6236467292,
]

def is_user_allowed(user_id):
    """检查用户 ID 是否在白名单中"""
    return user_id in ALLOWED_USER_IDS

def start_command(update: Update, context: CallbackContext) -> None:
    """处理 /start 命令，显示用户ID，并检查权限"""
    user_id = update.message.from_user.id
    if not is_user_allowed(user_id):
        update.message.reply_text("抱歉，你没有权限使用此机器人。")
        return  # 权限不足，直接返回，不执行后续操作

    update.message.reply_text(f"你的用户ID是: {user_id}")

def profile_command(update: Update, context: CallbackContext) -> None:
    """处理 /profile 命令，显示机器人Token，并检查权限"""
    user_id = update.message.from_user.id
    if not is_user_allowed(user_id):
        update.message.reply_text("抱歉，你没有权限使用此命令。")
        return

    # 安全提示：实际应用中不建议直接返回完整的 BOT_TOKEN
    update.message.reply_text(f"机器人API Token (已隐藏部分): {BOT_TOKEN[:8]}...")

def help_command(update: Update, context: CallbackContext) -> None:
    """处理 /help 命令，并检查权限"""
    user_id = update.message.from_user.id
    if not is_user_allowed(user_id):
        update.message.reply_text("抱歉，你没有权限查看帮助信息。")
        return

    help_text = """
    可用命令：
    /start - 显示你的用户ID
    /profile - 显示机器人API Token (仅显示部分)
    """
    update.message.reply_text(help_text)


def main() -> None:
    """启动机器人"""
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # 注册命令处理器
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("profile", profile_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
