import ytdl from "ytdl-core";

export const download = async (req,res)=> {
    const videoUrl = req.query.videoUrl;
    try {
        const info = await ytdl.getInfo(videoUrl);
        res.header("Content-Disposition", 'attachment; filename='+ info.videoDetails.title +".mp4");
        ytdl(videoUrl, {format: 'mp4'}).pipe(res);
    } catch (err) {
        console.log(err);
        throw err;
    }
}