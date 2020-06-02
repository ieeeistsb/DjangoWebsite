// @ts-ignore

export default class GetBranchImagesIO {

	public requestSerializer() {
		return '';
	}

	public responseSerializer(data) {

		const images_list : string[] = [];

		data.branch_images.forEach((image) => {
			images_list.push(image);
		});

		return images_list;
	}

	public errorSerializer(error) {
		return error;
	}
}
