from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid
from LuciferMoringstar_Robot.database.autofilter_db import is_subscribed, get_file_details
from LuciferMoringstar_Robot.database._utils import get_size
from translation import LuciferMoringstar
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS


@LuciferMoringstar_Robot.on_callback_query()
async def cb_handler(client: LuciferMoringstar_Robot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):


# ---------- π [ | ππ₯π’π¨π£ ππππ§ππ₯π¦ | ] π ---------- #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("β οΈhey {query.from_user.first_name}! This Is My Old Message So Please Request Again β οΈ",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="β οΈ CHECK BOT PM β οΈ", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page β‘", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="β οΈ CHECK BOT PM β οΈ", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("β οΈhey {query.from_user.first_name}! This Is My Old Message So Please Request Again β οΈ",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page β‘", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="β οΈ CHECK BOT PM β οΈ", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page β‘", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="β οΈ CHECK BOT PM β οΈ", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- π [ | ππ’π§ π£π  ππππ§ππ₯π¦ | ] π ---------- #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("β οΈhey {query.from_user.first_name}! This Is My Old Message So Please Request Again β οΈ",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page β‘", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("β οΈhey {query.from_user.first_name}! This Is My Old Message So Please Request Again β οΈ",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page β‘", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("π Back Page", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page β‘", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"π Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close ποΈ", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- π [ | πππ§ πππππ¦ | ] π ---------- #


        elif query.data.startswith("lucifermoringstar_robot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            f_caption=files.caption
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, file_name=title, file_size=size, file_caption=f_caption)
                except Exception as e:
                        print(e)
                f_caption=f_caption
            if f_caption is None:
                f_caption = LuciferMoringstar.FILE_CAPTIONS.format(mention=query.from_user.mention, title=title, size=size)
            
            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=f_caption
                        )
                    await query.answer('β οΈ Hey {query.from_user.first_name}! I have files in your PM please Check Bot pmβ οΈ ',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- π [ | π£π  πππππ¦ | ] π ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart π",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = LuciferMoringstar.FILE_CAPTIONS
                buttons = [[
                  InlineKeyboardButton('π₯οΈ Channel π₯οΈ', url=f'https://t.me/check_this_channel')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- π [ | π π’ππ¨πππ¦ | ] π ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("βοΈ Add me to βοΈ", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("βΉοΈ Help", callback_data="help"),
                 InlineKeyboardButton("π About", callback_data="about")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("βοΈ Add me to βοΈ", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("βΉοΈ Help", callback_data="bot_owner"),
                 InlineKeyboardButton("π About", callback_data="about")
                 ]]               
            await query.message.edit(text=START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("π  Home", callback_data="start"),
              InlineKeyboardButton("About π", callback_data="about")
              ]]               
            await query.message.edit(text=LuciferMoringstar.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("π  Home", callback_data="start"),
             InlineKeyboardButton("Close ποΈ", callback_data="close")
             ]]               
            await query.message.edit(text=LuciferMoringstar.ABOUT_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('π  Home', callback_data="start"),
             InlineKeyboardButton('About π', callback_data="about")
             ]]               
            await query.message.edit(text=LuciferMoringstar.PR0FESS0R_99.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "pages":
            await query.answer()

    else:
        await query.answer("β οΈ Hey, {query.from_user.first_name}! Search Your Own File, Don't Click Others Results π¬",show_alert=True)




