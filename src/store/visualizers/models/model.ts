import { IDataSourceModel } from 'src/store/data-sources/models/model';

export interface IVisualizer {
    data : IDataSourceModel,
    name : string,
    filters : any[],

}
