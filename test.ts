/*!
 * @Author: CPS
 * @email: 373704015@qq.com
 * @Date: 2022-05-23 21:03:01.195131
 * @Last Modified by: CPS
 * @Last Modified time: 2022-05-23 21:03:01.195131
 * @Projectname
 * @file_path "D:\CPS\MyProject\外接项目\PSD文件解析\psd-tools"
 * @Filename "test.ts"
 * @Description: 功能描述
 */

"use strict";

import axios from "axios";
import * as path from "path";
import * as fse from "fs-extra";

const tokenPath = path.resolve("./config/0523/jwt-token");
const configPath = path.resolve("./config/0523/config.json");

const TOKEN = fse.readFileSync(tokenPath).toString().replace("\r\n", "");

const config = fse.readJSONSync(configPath, { encoding: "utf8" });
const CLIENT_ID = config["API_KEY"];

const headers = {
  "Authorization": `Bearer ${TOKEN}`,
  "x-api-key": CLIENT_ID,
};

axios({
  url: "https://image.adobe.io/pie/psdService/hello",
  method: "get",
  proxy: false,
  headers,
})
  .then(res => {
    console.log(res.data);
  })
  .catch(err => {
    console.log(err);
  });
