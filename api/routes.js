import { Router } from 'express';
import {download} from './controller/downloadController.js'

const router = Router();

router.get("/download", download);

export default router;
