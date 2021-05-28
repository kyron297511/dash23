import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper # type: ignore

async def user(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    try:
        if not session["user_id"]: return aiohttp.web.HTTPForbidden()
    except KeyError:
        return aiohttp.web.HTTPForbidden()
    user = await userhelper.get_user(session["user_id"])
    if not "7" in str(user.privileges): return aiohttp.web.HTTPForbidden() # teach me how do do privileges relesto
    id = r.match_info["id"]
    return await utils.render_template(r, "admin/user.html", viewed_user=await userhelper.get_user(id))